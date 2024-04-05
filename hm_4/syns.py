

#                      СИНХРОННЫЙ ПОДХОД

arr_full = [87, 74, 87, 6, 46, 20, 98, 47, 42, 47, 100, 79, 7, 41, 92, 2, 90, 64, 52, 61, 31, 31, 88, 16, 60, 97, 68, 16, 35, 38, 32, 
            69, 76, 12, 37, 66, 6, 60, 51, 26, 93, 100, 70, 59, 72, 13, 48, 78, 8, 73, 64, 30, 20, 25, 50, 93, 38, 68, 31, 59, 23, 97, 
            16, 32, 67, 93, 90, 33, 37, 37, 72, 59, 45, 44, 82, 1, 3, 36, 69, 47, 93, 77, 24, 28, 9, 93, 11, 59, 10, 63, 81, 95, 8, 38, 
            56, 6, 52, 32, 14, 7, 80, 35, 54, 77, 79, 62, 24, 0, 0, 94, 70, 5, 14, 77, 7, 73, 22, 22, 90, 33, 18, 35, 19, 35, 76, 21, 72, 
            65, 54, 46, 11, 54, 7, 74, 80, 13, 65, 52, 1, 49, 12, 96, 62, 59, 28, 63, 88, 32, 33, 49, 25, 93, 10, 21, 74, 87, 0, 73, 85, 
            52, 52, 81, 79, 14, 9, 84, 84, 3, 41, 10, 12, 55, 73, 90, 73, 20, 20, 43, 99, 32, 2, 26, 27, 18, 39, 35, 43, 59, 3, 71, 74, 77, 
            25, 42, 82, 88, 11, 71, 21, 11, 93, 34, 47, 42, 58, 9, 8, 1, 92, 66, 73, 73, 26, 22, 12, 6, 73, 84, 30, 95, 32, 5, 31, 8, 11, 32, 
            25, 42, 81, 18, 77, 39, 6, 96, 89, 20, 92, 36, 59, 13, 79, 42, 38, 42, 50, 63, 63, 19, 71, 86, 17, 25, 4, 37, 60, 3, 26, 2, 68, 10, 
            47, 38, 29, 2, 52, 85, 68, 70, 61, 37, 34, 66, 27, 25, 84, 80, 1, 89, 88, 11, 95, 9, 33, 18, 98, 67, 89, 21, 74, 50, 90, 5, 17, 52, 
            6, 56, 97, 48, 62, 50, 5, 18, 24, 19, 1, 63, 73, 90, 59, 74, 95, 17, 21, 82, 16, 22, 81, 49, 67, 49, 6, 13, 29, 6, 18, 46, 48, 99, 
            53, 99, 41, 63, 82, 49, 85, 34, 21, 64, 2, 79, 47, 4, 27, 74, 19, 0, 51, 27, 90, 84, 49, 6, 27, 14, 81, 47, 34, 65, 85, 46, 35, 73, 
            28, 21, 29, 76, 0, 68, 25, 10, 60, 8, 82, 90, 82, 12, 60, 43, 37, 81, 40, 55, 69, 52, 32, 89, 60, 10, 92, 8, 43, 16, 72, 50, 18, 46, 
            64, 53, 69, 95, 91, 94, 24, 53, 82, 17, 90, 43, 51, 84, 99, 36, 55, 14, 70, 75, 2, 12, 61, 14, 48, 30, 2, 95, 31, 53, 36, 26, 52, 8, 
            27, 87, 87, 40, 63, 55, 55, 15, 55, 41, 62, 4, 81, 91, 28, 28, 14, 96, 26, 11, 36, 17, 97, 60, 75, 35, 6, 99, 91, 31, 62, 61, 36, 90, 
            63, 77, 7, 58, 23, 71, 86, 11, 45, 51, 67, 97, 8, 26, 49, 34, 47, 42, 28, 48, 54, 64, 57, 68, 71, 5, 8, 7, 0, 30, 16, 92, 21, 54, 77, 
            98, 58, 5, 3, 99, 4, 20, 59, 43, 11, 0, 27, 35, 11, 35, 57, 50, 54, 89, 40, 66, 57, 50, 42, 6, 61, 14, 25, 30, 78, 58, 1, 30, 55, 67, 
            46, 8, 3, 52, 73, 41, 22, 87, 2, 69, 8, 62, 60, 46, 30, 56, 73, 21, 71, 20, 34, 53, 18, 28, 62, 98, 37, 72, 48, 77, 50, 66, 95, 99, 
            35, 36, 94, 25, 75, 4, 84, 68, 66, 98, 94, 4, 16, 42, 76, 97, 29, 23, 54, 57, 21, 75, 87, 6, 96, 13, 51, 64, 79, 66, 33, 12, 70, 17, 
            99, 82, 22, 41, 27, 61, 65, 94, 83, 98, 24, 47, 48, 4, 77, 82, 13, 77, 96, 11, 63, 31, 31, 19, 43, 54, 58, 58, 67, 30, 91, 53, 97, 78, 
            63, 83, 45, 18, 26, 92, 64, 85, 59, 53, 49, 32, 21, 95, 50, 58, 5, 51, 72, 90, 49, 25, 82, 24, 46, 2, 62, 78, 61, 73, 30, 83, 56, 40, 
            5, 97, 42, 44, 83, 76, 75, 23, 62, 24, 45, 94, 97, 90, 36, 32, 1, 84, 14, 90, 50, 22, 44, 33, 69, 85, 53, 64, 52, 55, 6, 37, 42, 70, 
            89, 76, 3, 45, 13, 20, 12, 81, 71, 28, 31, 54, 17, 59, 42, 78, 92, 98, 10, 28, 73, 29, 23, 18, 24, 33, 14, 49, 60, 32, 23, 18, 68, 
            22, 52, 67, 56, 71, 20, 76, 10, 17, 51, 25, 9, 30, 59, 66, 75, 16, 3, 85, 29, 29, 98, 24, 96, 40, 82, 20, 23, 70, 80, 43, 47, 55, 11, 
            78, 12, 6, 24, 93, 58, 53, 74, 94, 85, 65, 2, 79, 68, 24, 1, 32, 61, 42, 6, 72, 58, 87, 87, 26, 49, 88, 77, 38, 17, 9, 64, 78, 99, 68, 
            79, 78, 41, 41, 35, 50, 93, 11, 65, 5, 43, 39, 39, 10, 50, 72, 55, 17, 67, 21, 95, 78, 59, 94, 14, 36, 69, 18, 81, 64, 59, 44, 69, 35, 
            31, 7, 59, 29, 88, 62, 77, 53, 17, 20, 95, 58, 96, 24, 51, 63, 14, 25, 80, 62, 5, 79, 28, 18, 74, 10, 98, 48, 21, 69, 28, 72, 52, 53, 
            20, 36, 14, 15, 69, 15, 22, 20, 5, 83, 91, 56, 5, 33, 7, 3, 3, 7, 67, 95, 20, 51, 86, 97, 24, 65, 46, 16, 10, 93, 96, 85, 51, 60,
            71, 85, 63, 61, 97, 8, 58, 83, 67, 52, 46, 49, 31, 58, 60, 4, 63, 96, 9, 56, 12, 35, 10, 81, 13, 70, 48, 73, 82, 36, 51, 60, 75, 79, 
            1, 49, 98, 33, 27, 58, 52, 24, 86, 20, 13, 47, 15, 31, 73, 24, 3, 14, 38, 65, 76, 29, 45, 23, 92, 92, 20, 91, 80, 24, 33, 72, 59, 17, 
            4, 40, 12, 14, 47, 9, 73, 12, 75, 65, 55, 14, 22, 52, 99, 81, 56, 67, 53, 7, 45, 66, 94, 92]

import time

start_time = time.time()
sum_of_random_nums = 0
cnt = 0

for i in arr_full:
    sum_of_random_nums += i
    cnt += 1
    print(f'Число {i} (порядковый номер: {cnt}), прибавляется к сумме {sum_of_random_nums}')
    print(f'Время вычисления{time.time() - start_time: .2f}')
print(f'Сумма чисел ровна = {sum_of_random_nums}')