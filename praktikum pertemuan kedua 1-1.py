def evaluate_performance(percentage):
    # Jika nilai persentase >= 90, kembalikan "Excellent performance"
    if percentage >= 90:
        return "Excellent performance"
    # Jika nilai persentase >= 80 dan < 90, kembalikan "Very Good performance"
    elif percentage >= 80:
        return "Very Good performance"
    # Jika nilai persentase >= 70 dan < 80, kembalikan "Good performance"
    elif percentage >= 70:
        return "Good performance"
    # Jika nilai persentase >= 60 dan < 70, kembalikan "Average performance"
    elif percentage >= 60:
        return "Average performance"
    # Jika nilai persentase < 60, kembalikan "Needs Improvement"
    else:
        return "Needs Improvement"

#Example usage
percentage = float(input("Enter the percentage: "))
result = evaluate_performance(percentage)
print(result)

#Function to find the largest number among three
def largest_of_three(a, b, c):
    # Menggunakan fungsi bawaan max() untuk mencari angka terbesar dari a, b, dan c
    return max(a, b, c)

#Example usage
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))
print("The largest number is:", largest_of_three(a, b, c))

#Function to print Fibonacci series up to n terms
n = int(input("Masukkan batas bilangan Fibonacci: "))  # Input batas Fibonacci dari user

a, b = 0, 1  # Inisialisasi nilai awal untuk dua angka pertama dalam deret Fibonacci
while a <= n:  # Selama nilai a masih lebih kecil atau sama dengan n
    print(a, end=" ")  # Cetak nilai a dan tetap di baris yang sama
    a, b = b, a + b  # Update nilai a dan b dengan rumus Fibonacci (a jadi b, b jadi a + b)
print("\n")  # Pindah baris setelah deret selesai dicetak

#Example usage
def cetak_angka_ganjil(n):
    # Menggunakan loop for untuk iterasi dari 1 sampai n
    for i in range(1, n + 1):
        # Jika i ganjil (sisa bagi 2 tidak nol), cetak i
        if i % 2 != 0:
            print(i, end=' ')  # Cetak i di baris yang sama
    print()  # Pindah baris setelah selesai mencetak angka ganjil

#Contoh penggunaan
n = int(input("Masukkan nilai n: "))
cetak_angka_ganjil(n)


#Function to print pattern based on n
def print_pattern(n):
    # Loop outer untuk iterasi dari 1 sampai n (baris)
    for i in range(1, n + 1):
        # Loop inner untuk mencetak i sebanyak i kali dalam satu baris
        for j in range(i):
            print(i, end=' ')  # Cetak nilai i di baris yang sama
        print()  # Pindah baris setelah satu pola selesai dicetak

#Example usage
n = int(input("Enter the value of n: "))
print_pattern(n)