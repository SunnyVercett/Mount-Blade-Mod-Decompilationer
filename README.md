# Mount-Blade-Mod-Decompilationer
A Mount&amp;Blade Game mod decompilationer that I wrote to alleviate the anger of having no source code of a favored mod.
I developed this on a Windows PC. So the batch file included is to fire the whole program.
It seems that the readme.md file is of specific purpose in Linux OS, only that I have no idea of the specifics.

Developed to decompile the mod "Prophery of Pendor" v3.611. Tested with the mod "Native" and "Shadow of Twisted Time". Global variables, quick strings and registers are included in the decompile process. Slot decompilation code still needs refine. This decompilation code needs original module-system to work, the header_*.py files to be specific. Put the files in this project and header files in module-system together in the same directory, and re-define the export path in module_info.py, then it's all set to decompile a module.
