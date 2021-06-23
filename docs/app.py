import dashboard_engine_docs as dbe_docs

app = dbe_docs.create_app()

server = app.server

if __name__ == "__main__":
    app.run_server(debug=True, port=5055)
