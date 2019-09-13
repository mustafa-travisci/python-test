def test_server_parallel_requests(printer, tmpdir):
    printer("create virtual environment into {}".format(tmpdir))
    create_virtual_environment(tmpdir)

    printer("start server from virtual env")
    start_server(tmpdir)

    printer("do the parallel request test")
    parallel_requests()
