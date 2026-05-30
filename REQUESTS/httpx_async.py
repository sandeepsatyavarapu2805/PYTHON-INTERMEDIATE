import httpx
import asyncio

async def main():
    # Create an asynchronous client session
    async with httpx.AsyncClient(base_url="https://httpbin.org") as client:
        try:
            # ------------------------ GET ------------------------
            payload_get = {'page': 2, 'count': 25}
            response_get = await client.get('/get', params=payload_get)
            response_get.raise_for_status()  # Check for 503/404 errors before parsing
            print(response_get.text)

            # ------------------------ POST ------------------------
            payload_post = {'username': 'Sandeep', 'password': 'testing'}
            response_post = await client.post('/post', data=payload_post)
            response_post.raise_for_status()  # Safety check
            print(response_post.text)

            # Safe to decode now because raise_for_status confirmed 200 OK
            r_json = response_post.json()
            print(r_json['form'])
            print()

            # ------------------------ AUTH ------------------------
            response_auth = await client.get('/basic-auth/Sandeep/testing', auth=('Sandeep', 'testing'))
            response_auth.raise_for_status()
            print(response_auth.text)

            # Note: We intentionally skip raise_for_status here because we want to see the 401 response object
            response_unauth = await client.get('/basic-auth/Sandeep/testing', auth=('sandeep', 'testing'))
            print(response_unauth)

            # ------------------------ DELAY-TIMEOUT ------------------------
            response_delay = await client.get('/delay/1', timeout=4.0)
            response_delay.raise_for_status()
            print(response_delay)

        except httpx.HTTPStatusError as exc:
            print(f"\n❌ Async Server Error Encountered: {exc.response.status_code}")
            print("The server is currently struggling or under maintenance. Try again in a few moments.")
            
        except httpx.TimeoutException as exc:
            # Catching ConnectTimeout, ReadTimeout, and WriteTimeout
            print(f"\n❌ Async Timeout Error: The server took too long to respond ({type(exc).__name__}).")
            
        except httpx.RequestError as exc:
            # Catching connection issues (e.g. no internet)
            print(f"\n❌ Async Network Error: Could not connect to host: {exc}")

# This line kicks off the async event loop to run the code
asyncio.run(main())