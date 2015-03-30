import email
import wave


def main():
    mail = email.message_from_file(open('bin.txt'))
    for part in mail.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        indians = open('indian.wav', 'wb')
        indians.write(part.get_payload(decode=True))
        indians.close()
        break

    wave_in = wave.open('indian.wav', 'rb')
    wave_out = wave.open('indian2.wav', 'wb')
    wave_out.setparams(wave_in.getparams())

    for i in range(wave_in.getnframes()):
        wave_out.writeframes(wave_in.readframes(1)[::-1])

    wave_out.close()


if __name__ == '__main__':
    main()
