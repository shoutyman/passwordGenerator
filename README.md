# shoutyman's Password Generator

python generator.py -h

This is a simple passphrase/password generator, utilizing Python's _secrets_ module.
Similar programs exist on the Internet, but I thought it would be fun to create my own.

# Dependencies

The generator is dependent on pyperclip for clipboard functionality.

The generator requires a list of words to read from. By default the generator looks for a file named 'dictionary.txt', but this can be overridden with the --dictionary option. In general, the longer the word list and the longer the words in the list, the more secure the generated passphrase.
