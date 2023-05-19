import csv
import datetime
import os

async def log_request(request, log_folder):
    # Create log folder if it doesn't exist
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # Get current date and time
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    # Write log to CSV file
    csv_path = os.path.join(log_folder, f"{date_str}.csv")
    with open(csv_path, "a", newline="") as csv_file:
        body = await request.body()
        writer = csv.writer(csv_file)
        writer.writerow([date_str, time_str, request.method, request.url.path, dict(request.headers), body.decode()])

    # Write log to text file
    txt_path = os.path.join(log_folder, f"{date_str}.txt")
    with open(txt_path, "a") as txt_file:
        txt_file.write(f"time: {date_str + ' ' + time_str}\nmethod: {request.method}\npath: {request.url.path}\nheaders: {dict(request.headers)}\nbody: {body.decode()}\n\n")