import speedtest

def test_speed():
    print("Testing network speed... Please wait.")
    
    st = speedtest.Speedtest()
    
    # Get best server
    st.get_best_server()

    # Test download speed
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    
    # Test upload speed
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    
    # Get ping
    ping = st.results.ping

    # Display results
    print(f"\n📡 Network Speed Test Results 📡")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

if __name__ == "__main__":
    test_speed()
