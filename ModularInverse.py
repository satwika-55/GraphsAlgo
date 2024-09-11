def mod_inverse(x, mod):
    # Fermat's little theorem states that a^(mod-2) is the modular inverse of a when mod is prime
    return pow(x, mod - 2, mod)
