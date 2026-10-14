# === TRY / EXCEPT BLOCKS

# try     : test code for errors
# except  : handle the error
# else    : execute code when there is no error
# finally : execute code regardless of error or not

try:
    #True
    raise IndexError("This is an index error")
except IndexError as e:
    print(f"{e}, but it was caught and aborted!")
except (TypeError, NameError):
    pass
else:
    print("All good!")
finally:
    print("We can clean up resources here")