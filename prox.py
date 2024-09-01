import pexpect
# Login
child = pexpect.spawn('ssh elnur@192.168.209.130 -D 1080')
child.expect("password:")
child.sendline('elnur')
# Ensure Interface appeared
child.expect(r'elnur@elnur:~\$')
child.sendline('ip -c=always a show gpd0')
child.expect(r'elnur@elnur:~\$')
print(child.before.decode())
# End Connection
input("Press Enter to Stop The Proxy")
child.sendline('logout')
child.expect(pexpect.EOF)


