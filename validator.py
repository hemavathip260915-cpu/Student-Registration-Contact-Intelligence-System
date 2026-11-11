def validate_contact(name, phone, email):
    """Return (True, 'Valid') or (False, reason) for one contact."""
    name = (name or "").strip()
    phone = (phone or "").strip()
    email = (email or "").strip()

    if not name:
        return False, "Missing name"
    if len(phone) != 10 or not phone.isdigit() or phone[0] not in "6789":
        return False, "Invalid phone"
    if email.count("@") != 1:
        return False, "Bad email: must contain exactly one @"
    if any(ch.isspace() for ch in email):
        return False, "Bad email: contains whitespace"
    local, domain = email.split("@")
    if not local:
        return False, "Bad email: missing text before @"
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False, "Bad email: domain must contain an internal period"
    return True, "Valid"
