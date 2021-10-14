from app import app
import socket


def isNetOK(testserver):
    s = socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            ret_value = True
        else:
            ret_value = False
    except Exception as e:
        error_class = e.__class__.__name__  # 取得錯誤類型
        detail = e.args[0]  # 取得詳細內容
        print('[{}] {}'.format(error_class, detail))
        ret_value = False
    return ret_value


def isNetChainOK(testserver=('8.8.8.8', 443)):
    isOK = isNetOK(testserver)
    return isOK


if __name__ == '__main__':
    # if isNetChainOK():

    app.run(host='0.0.0.0', port=5218, debug=False)
    #app.run(host='127.0.0.1', port=5120, debug=True)
    # else:
    #    print('The network is NOT work!')
