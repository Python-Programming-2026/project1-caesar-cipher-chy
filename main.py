def caesar_encrypt(text, shift):
    shift = shift % 26
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= ch <= 'Z':
            new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(ch)

    return ''.join(result)


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


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
