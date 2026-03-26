
letter = ''' Dear <|Name|>,
        You are selected!
        <|Date|> '''

print(letter.replace("<|Name|>","Raman").replace(" <|Date|>","24 march 2026"))
