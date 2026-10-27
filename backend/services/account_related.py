
def _get_owned_account_or_403(tag: str, user, db):
    """Raise 403 unless `tag` is one of this user's linked accounts."""
    print("tag",tag)
    if tag not in [a.tag for a in user.accounts]:
        raise HTTPException(status_code=403, detail="This account is not linked to your user")