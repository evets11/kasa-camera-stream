# Kasa-Camera

Based on https://github.com/joshgetter/hassio-addons/tree/master/kasa-camera

## Introduction
This app allows KC100 (and similar) cameras to be streams via web URL.

## Configuration
### General
When you initially set up a Kasa camera, the Kasa app will have you create an account. You will need to provide these credentials to allow the add-on to access the stream.

The following is a description of each configuration item.

`kasausername` - **Required**. The username for your Kasa account. This should be an email address.

`kasapassword` - **Required**. The password for your Kasa account.

`cameraip` - **Required**. The IP address of the Kasa camera. _Note:_ Ideally the camera will have a reserved / static IP so that this doesn't need to be updated.

`cameraname` - Default: "kasacam". The name of the camera. This will impact the URL of the output streams.

copy the example options file and enter your details.

`cp data/options.json.example data/options.json`

Example configuration:
``` json
{
  "kasausername": "user@example.com",
  "kasapassword": "password1234",
  "cameraip": "192.168.1.2",
  "cameraname": "livingroom"
}
```

### Network
Docker compose exposes two ports. One for RTMP video output, and one for HTTP output.  By default they will be mapped in the following way, so that they don't conflict with the typical HTTP and RTMP ports on your host system.  Feel free to change these as needed.

```
1935/tcp: 43331 (exposes RTMP on port 43331 on the host)
80/tcp: 43330 (exposes HTTP on port 43330 on the host)
```

## Running
`docker-compose up -d`

## Output
The add-on will expose the camera video as a stream in the following formats:
* HLS - `http://<IP>:43330/hls/<CAMERA NAME>.m3u8`
* RTMP - `rtmp://<IP>:43331/live/<CAMERA NAME>`

Thumbnails will be generated from the camera. The latest thumbnail image can be accessed at:
* Thumbnail - `http://<HA IP>:43330/thumbnails/<CAMERA NAME>.jpg`

## Adding Camera to Home Assistant
You can add the camera to Home Assistant using the above output streams.  This demonstrates how you'd add a camera based on the example configuration above:

``` yaml
stream:
camera:
  - platform: generic
    name: "Living Room Camera"
    still_image_url: "http://<HA IP>:43330/thumbnails/livingroom.jpg"
    stream_source: "http://<HA IP>:43330/hls/livingroom.m3u8"
```