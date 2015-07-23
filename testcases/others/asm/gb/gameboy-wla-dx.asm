
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; a simple parallax scroller for game boy and wla-macro assembler
; written by ville helin <vhelin@cc.hut.fi> in 1998-2000
; requires wla-gb v6.0+
; works on a real game boy
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»

.MEMORYMAP
SLOTSIZE $4000
DEFAULTSLOT 0
SLOT 0 $0000
SLOT 1 $4000
.ENDME

.ROMBANKSIZE $4000
.ROMBANKS 2


.NAME "SINAAPPI"
.RAMSIZE 0
.EMPTYFILL $c9				;ret.
.CARTRIDGETYPE 1
.LICENSEECODEOLD $00
.COMPUTECHECKSUM
.COMPUTECOMPLEMENTCHECK




;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; interrupts
; these can be relocated in realtime as they all reside in RAM.
; (vbi jumps to $c000 where yet another jump is made).
; all interrupts cost this way one additional JP, but are very flexible.
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»


.ORG $40				;vbi.
	JP	$C000
.ORG $48				;lcd stat.
	JP	$C003
.ORG $50				;timer.
	JP	$C006
.ORG $58				;serial.
	JP	$C009
.ORG $60				;high to low.
	JP	$C00C

;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; standard beginning
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»

.ORG $100

	NOP
	JP	MAIN

;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; global definitions
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»

.ENUM $C041
palette_counter    DB
palette_index      DB
palette_number     DB
vbi_counter        DB
lcd_scx_1          DB
lcd_scx_2          DB
lcd_scx_3          DB
vbi_scroll_counter DB
.ENDE

.DEFINE letter_translation_table $C100	;takes 256 bytes.

;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; main
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»

.ORG $150

MAIN:	DI
	LD	SP, $FFFE

	LD	HL, $C000		;empty interrupts.
	LD	A, $D9			;reti.
	LD	BC, 3
	LD	(HL), A
	ADD	HL, BC
	LD	(HL), A
	ADD	HL, BC
	LD	(HL), A
	ADD	HL, BC
	LD	(HL), A
	ADD	HL, BC
	LD	(HL), A

	CALL	WAIT_VBI

	LD	A, %10000001
	LDH	(R_LCDC), A		;lcd control.

	XOR	A
	LDH	(R_BGP), A		;background palette.
	LDH	(R_SCY), A		;background y.
	LDH	(R_SCX), A		;background x.

	LD	HL, $C000
	LD	A, $C3			;jp.
	LDI	(HL), A
	LD	BC, VBI_PALETTE

	LD	A, C
	LDI	(HL), A
	LD	A, B
	LD	(HL), A			;vbi.

	LD	HL, $C003
	LD	A, $C3			;jp.
	LDI	(HL), A
	LD	BC, LCD_SCROLL_1
	LD	A, C
	LDI	(HL), A
	LD	A, B
	LD	(HL), A			;lcd.

	LD	A, %11
	LDH	(R_IE), A		;enable vbi & lcd.
	LD	A, %01000000
	LDH	(R_STAT), A		;lcd cmp irq.
	LD	A, $77
	LDH	(R_LYC), A

	XOR	A
	LD	HL, vbi_counter
	LD	(HL), A			;reset vbi counter.
	LD	HL, palette_number
	LD	(HL), A			;reset palette number.
	LD	HL, palette_index
	LD	(HL), A			;reset palette index.
	LD	HL, palette_counter
	LD	(HL), A			;reset palette counter.
	LD	HL, lcd_scx_1
	LD	(HL), A			;reset scroll counter.
	LD	HL, lcd_scx_2
	LD	(HL), A			;reset scroll counter.
	LD	HL, lcd_scx_3
	LD	(HL), A			;reset scroll counter.

	LD	HL, $9800		;tiles.
	LD	B, 4
	LD	C, L			;4 * 256 bytes.
	LD	A, $FF
	CALL	SET_RAM

	LD	HL, $8800		;tile data.
	LD	B, 16
	LD	C, L			;16 * 256 bytes.
	XOR	A
	CALL	SET_RAM

	EI


;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; delay loop
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»

	LD	HL, vbi_counter
	
_LOOP_1:
	HALT
	NOP
	LD	A, (HL)
	CP	60
	JR	NZ, _LOOP_1		;wait for one second.

;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; create scrolling background
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»

	CALL	WAIT_VBI

	LD	HL, $9A20
	LD	B, 4

LOOP_E:	LD	C, 8
	LD	A, 41

LOOP_E_1:
	LDI	(HL), A
	INC	A
	DEC	C
	JR	NZ, LOOP_E_1

	DEC	B
	JR	NZ, LOOP_E

	LD	HL, $9A00
	LD	B, 4

LOOP_F:	LD	C, 8
	LD	A, 49

LOOP_F_1:
	LDI	(HL), A
	INC	A
	DEC	C
	JR	NZ, LOOP_F_1

	DEC	B
	JR	NZ, LOOP_F

	LD	HL, $99E0
	LD	B, 4

LOOP_G:	LD	C, 8
	LD	A, 57

LOOP_G_1:
	LDI	(HL), A
	INC	A
	DEC	C
	JR	NZ, LOOP_G_1

	DEC	B
	JR	NZ, LOOP_G

	LD	HL, vbi_counter

LOOP_2:	HALT
	NOP
	LD	A, (HL)
	CP	180
	JP	NZ, LOOP_2		;wait for three seconds.

	LD	HL, vbi_scroll_counter
	LD	A, $1
	LD	(HL), A

	LD	HL, $C001		;change to scroll vbi.
	LD	BC, VBI_SCROLL_1
	LD	A, C
	LDI	(HL), A
	LD	A, B
	LD	(HL), A			;vbi.

END:	HALT
	NOP
	JP	END

;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; output text
; DE = input
; HL = output
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»

OUTPUT_TEXT:
	LD	BC, 32

OUTPUT_TEXT_LOOP:
	LD	A, (DE)
	INC	DE
	OR	A
	JR	Z, OUTPUT_TEXT_END
	CP	$A
	JR	Z, OUTPUT_TEXT_NEXT_LINE

	DEC	BC
	PUSH	BC
	LD	BC, letter_translation_table
	LD	C, A
	LD	A, (BC)
	POP	BC

	LDI	(HL), A
	JR	OUTPUT_TEXT_LOOP

OUTPUT_TEXT_NEXT_LINE:
	ADD	HL, BC
	CALL	WAIT_VBI
	JR	OUTPUT_TEXT

OUTPUT_TEXT_END:
	RET
	
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; set memory
; A  = byte to set the memory to
; HL = output start
; BC = amount of bytes (B * C)
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»

SET_RAM:
	LD	D, C

	CALL	WAIT_VBI

SET_RAM_LOOP:
	LDI	(HL), A
	DEC	C
	JR	NZ, SET_RAM_LOOP
	LD	C, D			;return the counter.
	
	CALL	WAIT_VBI

	DEC	B
	JR	NZ, SET_RAM_LOOP

	RET

;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; copy 8x8 tile data
; HL = output
; DE = input
; B  = amount of 8x8 tiles
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»

COPY_8X8:
	LD	C, 16

COPY_DATA:
	LD	A, (DE)
	INC	DE
	LDI	(HL), A

	DEC	C
	JR	NZ, COPY_DATA

	CALL	WAIT_VBI

	DEC	B
	JR	NZ, COPY_8X8
	RET

;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; palette vbi
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»

.ORG $1000

.DEFINE palette_index_max 4
.DEFINE palette_change_delay 6

VBI_PALETTE:
	PUSH	AF
	PUSH	HL

	LD	HL, palette_counter
	INC	(HL)
	LD	A, (HL)
	CP	palette_change_delay
	JR	NZ, VBI_PALETTE_EXIT	;dont update the palette this frame.

	XOR	A
	LD	(HL), A			;reset counter.

	LD	HL, palette_index	;load palette base.
	LD	A, (HL)

	CP	palette_index_max
	JR	Z, VBI_PALETTE_EXIT	;last index reached already.

	INC	(HL)			;increment palette index.

	LD	HL, palette_number
	ADD	(HL)
	LD	HL, PALETTE_TABLES
	ADD	L
	LD	L, A

	LD	A, (HL)
	LDH	(R_BGP), A

VBI_PALETTE_EXIT:
	LD	HL, vbi_counter
	INC	(HL)

	XOR	A
	LDH	(R_SCX), A

	POP	HL
	POP	AF
	RETI

;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; scroll vbi
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»

VBI_SCROLL_1:
	PUSH	AF
	PUSH	HL

	LD	HL, vbi_counter
	INC	(HL)

	XOR	A
	LDH	(R_SCX), A

	LD	HL, vbi_scroll_counter
	DEC	(HL)
	JP	NZ, VBI_SCROLL_1_EXIT
	LD	A, $1
	LD	(HL), A

	LD	HL, lcd_scx_1
	DEC	(HL)
	DEC	(HL)
	DEC	(HL)
	LD	HL, lcd_scx_2
	DEC	(HL)
	DEC	(HL)
	LD	HL, lcd_scx_3
	DEC	(HL)

VBI_SCROLL_1_EXIT:
	POP	HL
	POP	AF
	RETI


;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
; palette data
;»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»

.ORG $1100

PALETTE_TABLES:
	;must be at $xx00 address.

	.DB %00000000 %01010101 %10101010 %11111111
	;to black from white

	.DB %11111111 %10101011 %01011011 %00011011
	;to %00011011 from black

	.DB %00011011 %01011011 %10101011 %11111111
	;to black from %00011011

FONT_UPPERCASE:
	.DB 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ;i forgot the space...

START_TXT_1:
	.DB " A SIMPLE PARALLAX  " $A
	.DB "      SCROLLER      " $A
	.DB "                    " $A
	.DB "CODED BY VILLE HELIN" $A
	.DB "   IN 1998-2000!    " $A
	.DB "                    " $A
	.DB "                    " $A
	.DB "                    " $A
	.DB "                    " $A
	.DB "               PYON!" $A
	.DB "                    " $A
	.DB 0
