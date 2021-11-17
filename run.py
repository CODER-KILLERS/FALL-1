import sys, os, subprocess


if sys.version[0:3] != "3.9":
  sys.exit(" [!] Anda harus menggunakan versi python 3.9, versi python anda sekarang : "+sys.version[0:3])

if __name__ == "__main__":
  try:
    os.system("git pull")
    __import__("fmbf").menu()
  except Exception:
      os.system("git pull")
      __import__("fmbf").menu() 