street = "stra\N{LATIN SMALL LETTER SHARP S}e"
street_input = "STRASSE"

# upperで比較するとOK、lowerはNG。文字によっては結果が安定しない。
print("upper", street_input.upper() == street.upper())
print("lower", street_input.lower() == street.lower())

# casefoldが良い。
print("casefold", street_input.casefold() == street.casefold())
