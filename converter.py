from Engine import *
import sys

if __name__ == "__main__":
	print("=" * 90)

	if  not len(sys.argv) > 1:
		filename = input("Введите название файла для конвертации без расширения: ")
	else:
		filename = sys.argv[1].split("\\")[-1].split(".")[0]

	input(f"Внимание! Файл {filename}.ebm будет перезаписан при наличии в папке. Если согласны нажмите Enter.")
	print("Запущен процесс конвертации, пожалуйста ожидайте...")
	
	try:
		print("Распаковка")
		bmp = BMP(filename + ".bmp")
		print("Создание")
		ebm = EBM(bmp.buffer)
		print("Сохранение")
		ebm.saveToFile(filename + ".ebm")
		print(f"Файл {filename} успешно сконвертирован в EBM. Нажмите Enter для выхода.")
	except:
		print("При конвертации произошла ошибка. Попробуйте другой файл. Нажмите Enter для выхода.")

	input("=" * 90)