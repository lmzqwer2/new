all: ./dist/new config.json
./dist/new:
	pyinstaller -F new.py
config.json
	echo '{\n\t"emptyFile":"emptyFile"\n}' > config.json
install: config.json ./dist/new ~/Templates/
	cp ./dist/new ~/bin/new
	cp config.json ~/Templates/.config.json
~/Templates/:
	mkdir ~/Templates
uninstall:
	rm ~/bin/new
clean:
	rm -rf new.spec config.json dist/ build/

.PHONY: all install uninstall clean
