import base64
import urllib

import requests

API_KEY = "P81wqwORR0OQjBoANWh3TMIj"
SECRET_KEY = "0xqj2amMnkmld93sSEw0VpVMHrpipR95"


def return_local(text, picpath):
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token=" + get_access_token()

    # image 可以通过 get_file_content_as_base64("C:\fakepath\jiangkang.jpg",True) 方法获取
    # image = get_file_content_as_base64("../Scripts/screenshot.png",True)
    image = get_file_content_as_base64(picpath, True)

    payload = f'image={image}&detect_direction=false&vertexes_location=false&paragraph=false&probability=false&char_probability=false&multidirectional_recognize=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    # 这段为自定义，目的是获取response中的坐标
    if response.status_code == 200:
        ocr_result = response.json()
        print(ocr_result)
        if 'words_result' in ocr_result:
            for item in ocr_result['words_result']:
                if item['words'] == text:
                    x = item['location']['left'] + item['location']['width'] // 2
                    y = item['location']['top'] + item['location']['height'] // 2
                    return (x, y)
    return '未找到元素'


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    print(return_local('每日活动'))
