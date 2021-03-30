import requests
import pytest
res = requests.get("http://www.baidu.com")

res = requests.post("http://httpbin")
print(res.text)

if __name__ == '__main__':
    pytest.main()