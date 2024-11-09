def test_home():
    response=app.test_client().get("/")

    assert response.status_code==200
    assert response.data== b"TIU is the best university"
 
