import httpx

with httpx.Client(base_url="https://httpbin.org") as client:
    try:
        # ------------------------ GET ------------------------
        payload_get = {'page': 2, 'count': 25}
        response_get = client.get('/get', params=payload_get)
        response_get.raise_for_status()  
        print(response_get.text)

        # ------------------------ POST ------------------------
        payload_post = {'username': 'Sandeep', 'password': 'testing'}
        response_post = client.post('/post', data=payload_post)
        response_post.raise_for_status()  
        print(response_post.text)

        r_json = response_post.json()
        print(r_json['form'])
        print()

        # ------------------------ AUTH ------------------------
        response_auth = client.get('/basic-auth/Sandeep/testing', auth=('Sandeep', 'testing'))
        response_auth.raise_for_status()
        print(response_auth.text)

        response_unauth = client.get('/basic-auth/Sandeep/testing', auth=('sandeep', 'testing'))
        print(response_unauth) 

        # ------------------------ DELAY-TIMEOUT ------------------------
        response_delay = client.get('/basic-auth/delay/1', timeout= 4)
        response_delay.raise_for_status()
        print(response_delay)

    except httpx.HTTPStatusError as exc:
        print(f"\n❌ Server Error Encountered: {exc.response.status_code}")
        print("The server is currently unavailable. Please try running the script again later.")
        
    except httpx.TimeoutException as exc:
        # This will now catch ReadTimeout, ConnectTimeout, and WriteTimeout perfectly!
        print(f"\n❌ Timeout Error: The server took too long to respond ({type(exc).__name__}).")
        
    except httpx.RequestError as exc:
        # Catch-all for other rare network errors (like no internet connection)
        print(f"\n❌ Network Error: An error occurred while handling your request: {exc}")