def convert_bytes(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:

        if size < 1000:

            return f"{size:.2f} {unit}"

        size /= 1000

    return f"{size:.2f} PB"

if __name__ == "__main__":
    convert_bytes()