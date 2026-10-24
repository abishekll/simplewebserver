from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>sample web page</title>
    </head>
        <body>
            <h1 bgcolor="red">Name=ABISHEK L </h1>
            <h2 bgcolor="red">REF NO=26014575</h2>
            <table border="2" bgcolor="yellow" cellspacing="10" cellpadding="10" >
                <caption>LAPTOP CONFIGURATION</caption>
                <tr>
                    <th bgcolor="beige">s.no</td>
                    <th bgcolor="beige">device type</td>
                    <th bgcolor="beige">device info</td>
                </tr>
                <tr>
                    <td bgcolor="beige">1</td>
                    <td bgcolor="beige" align="center">Device Name</td>
                    <td bgcolor="beige" align="center">TL15-53M-G2</td>
                </tr>
                <tr>
                    <td bgcolor="beige">2</td>
                    <td bgcolor="beige" align="center">Processor</td>
                    <td bgcolor="beige" align="center">intel(R) core(TM) 5210H(2.20 GHZ)</td>
                </tr>
                <tr>
                    <td bgcolor="beige">3</td>
                    <td bgcolor="beige" align="center">Istalled RAM</td>
                    <td bgcolor="beige" align="center">16.0 GB (15.7GB usable)</td>
                </tr>
                <tr>
                    <td bgcolor="beige">4</td>
                    <td bgcolor="beige" align="center">Graphics Card</td>
                    <td bgcolor="beige" align="center">intel(R) Graphics (128 MB)</td>
                </tr>
                <tr>
                    <td bgcolor="beige">5</td>
                    <td bgcolor="beige" align="center">Storage</td>
                    <td bgcolor="beige" align="center">477 GB total(115 gb used)</td>
                </tr>
                <tr>
                    <td bgcolor="beige">6</td>
                    <td bgcolor="beige" align="center">Device ID</td>
                    <td bgcolor="beige" align="center">0C8C0591-AFF1-4FD1-81FE-2063F09AF79C</td>
                </tr>
                <tr>
                    <td bgcolor="beige">7</td>
                    <td bgcolor="beige" align="center">product ID</td>
                    <td bgcolor="beige" align="center">00342-42945-11520-AAOEM</td>
                </tr>
                <tr>
                    <td bgcolor="beige">8</td>
                    <td bgcolor="beige" align="center">system type</td>
                    <td bgcolor="beige" align="center">64-bit operating system,x64-based processor</td>
                </tr>
                <tr>
                    <td bgcolor="beige">9</td>
                    <td bgcolor="beige" align="center">pen and touch support</td>
                    <td bgcolor="beige" align="center">No pen or touch input is available for this display</td>
                </tr>
            </table>

        </body>
        
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()