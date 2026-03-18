def caesar_encrypt(text, shift):
    """
    加密函数，本程序的核心函数
    本质是对一段字符串的每个字符进行偏移处理
    """
    shift = shift % 26 #对偏移量取余保证字母经处理后任是字母
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
            """
            对于小写字母
            使用ord()计算偏移量再使用chr()复原为字符
            使用.append()将处理好的字母加入result末尾
            """
        elif 'A' <= ch <= 'Z':
            new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
            #对于大写字母同理
        else:
            result.append(ch)
            #对于其他字符如空格不进行处理

    return ''.join(result)


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
    """
    解密的本质也是对一段字符串的每个字符进行偏移处理
    直接套用 caeser_encrypt() 的代码
    将偏移量取负以达到解密的目的
    """


def caesar_brute_force(ciphertext):
    results = {}
    for shift in range(26):
        results[shift] = caesar_decrypt(ciphertext, shift)
    return results


 

if __name__ == "__main__":
    while True:
        print("1. 加密")
        print("2. 解密")
        print("3. 暴力破解")
        print("4. 退出")
        choice = input("请选择功能: ")
        if choice == "1":
            text = input("请输入明文: ")
            shift = int(input("请输入偏移量: "))
            result = caesar_encrypt(text, shift)
            print("加密结果:", result)
        elif choice == "2":
            text = input("请输入密文: ")
            shift = int(input("请输入偏移量: "))
            result = caesar_decrypt(text, shift)
            print("解密结果:", result)
        elif choice == "3":
            text = input("请输入密文: ")
            results = caesar_brute_force(text)
            print("所有可能结果：")
            for shift, value in results.items():
                print("偏移量", shift, ":", value)
        elif choice == "4":
            print("程序结束")
            break
        else:
            print("输入错误，请重新选择")