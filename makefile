all:
	pyinstaller -F new.py
	echo '{\n\t"emptyFile":"emptyFile"\n}' > config.json
install: config.json ./dist/new ~/.lnewtemplate/
	cp ./dist/new ~/bin/new
	cp config.json ~/.lnewtemplate/config.json
~/.lnewtemplate/:
	mkdir ~/.lnewtemplate
uninstall:
	rm ~/bin/new
	rm -rf ~/.lnewtemplate
clean:
	rm -rf new.spec config.json dist/ build/

.PHONY: all install uninstall clean
