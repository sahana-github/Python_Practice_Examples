from io import call
call(["amixer", "-D", "pulse", "sset", "Master", "0%"])
