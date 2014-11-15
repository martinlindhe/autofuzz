SETUP:
  pip3 install psutil


"c++ dependencies build system"
XXX det finns andra såna gär projekt
minsta bästa planen kunde vara att anpassa google Go's pakethanterare för c/c++ ?
   --- istället! skulle kunna göra ett ramverk för att enkelt fuzza foss-program
       med detta (?) första target: afl, stöd flera fuzzers, etc




in what lang? C# or Python3?


python3:
	NEED: OS class: am i running win/linux/mac?
	NEED: class that find system compilers: gcc, llvm/clang
	NEED: homebrew-like recipes, in code, extend from Recipe class
	NEED: in recipe, compile from source instructions
	NEED-later: in recpie, install pre-build binary (?)
	NEED: generate cmake-file for your project using a project recipe:
		proj recipe: project name, dependencies and additional steps to take when building
		"cppdep update" will update depencencies, if needed
		"cppdep check" will check if dependencies are met
		"cppdep doctor" will point out if xcode is too old, XXX detect xcode version



C# built build system for c++ projects

recipe that describe a library, how to build it from source, similar to homebrew
cli tool to query recipes (use homebrew git model?)
main target: OSX
use cmake!?
ability to specify in own “recipe” what dependencies are needed for my software
serve pre-built (& gpg signed) binaries for packages
target llvm/clang first
also target C ?

start out by offering a small set of ready libs:
libsdl, libsdl2 (?)
allegro
opencv


question: http://programmers.stackexchange.com/questions/170679/why-are-there-no-package-management-systems-for-c-and-c
