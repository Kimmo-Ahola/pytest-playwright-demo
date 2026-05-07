# capitalize() och title() finns redan i Python men vi gör våra egna

# -> str = returns a string kallas för type hint
# en type hint är ett "förslag" på vad funktionen ska returnera
# text: str = tar in en textsträng
def my_capitalize(text: str | None) -> str:
    """
    Denna ska 'motsvara' pythons capitalize()
    Capitalize tar en input-sträng, omvandlar input så att
    första bokstaven blir stor och resten blir små
    """
    if not text:
        return ""
    
    lowered = text.lower().strip()

    for i, ch in enumerate(lowered):
        if ch.isalpha():
            return lowered[:i] + ch.upper() + lowered[i+1:]
    
    return lowered

def my_title() -> str :
    """
    Ska baseras på pythons title()
    Om man skickar in: "KIMMO AHOLA" får man "Kimmo Ahola"

    Om man skickar in britt-marie ska man få Britt-Marie eller Britt-marie
    Om man skickar in o'connor ska man få O'Connor

    tips: 
    import string 
    string.punctuation
    """
    # import string
    # string.punctuation
    raise NotImplementedError()