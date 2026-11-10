# Another user cannot read the owner's rating.
def test_other_user_cannot_read_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.get(path, headers=other_auth)
    print("Read:", res.status_code)
    assert 400 <= res.status_code <= 499

    check = api.get(path, headers=auth)
    assert check.status_code == 200
    assert check.json() == rating


# Another user cannot update the owner's rating.
def test_other_user_cannot_update_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.put(path, json={"stars": 5}, headers=other_auth)
    print("Update:", res.status_code)
    assert 400 <= res.status_code <= 499

    check = api.get(path, headers=auth)
    assert check.status_code == 200
    assert check.json() == rating


# Another user cannot delete the owner's rating.
def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.delete(path, headers=other_auth)
    print("Delete:", res.status_code)
    assert 400 <= res.status_code <= 499

    check = api.get(path, headers=auth)
    assert check.status_code == 200
    assert check.json() == rating