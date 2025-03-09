## New Orleans (10 pts)
`447e: <create_password>` creates the same static password at address `0x2400` every time it runs
`44b2: <get_password>` gets a password from the user and stores it at address `0x439b`
`44bc: <check_password>` checks the entered password stored in memory to the actual byte by byte
Solution: - Not the same thing every time. First, run the program up to the `<get_password>` function. When it asks for input, press wait, and look at the value in `0x2400`