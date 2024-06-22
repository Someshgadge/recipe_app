def test_create_recipe(test_client, auth):
    auth.login()
    response = test_client.post('/recipe/new', data=dict(
        title='Test Recipe',
        description='Test Description',
        ingredients='Test Ingredients',
        instructions='Test Instructions'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Recipe created successfully!' in response.data
