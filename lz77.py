'''
    - implements lz77 compress/decompress
    - infinite look head
    - inefficient complexity implementation
'''



class LZ77(object):
    def __init__(self, min_sequence, window_size):
        self.min_sequence = min_sequence
        self.window_size = window_size

    def compress(self, data):

        compressed_data = ''
        window = ''

        i = 0
        while i < len(data):
            seq_len = 1
            while i + seq_len <= len(data) and seq_len <= window and data[i:i+seq_len] in window:
                seq_len += 1

            seq_len -= 1
            if seq_len >= self.min_sequence and data[i:i+seq_len] in window:
                offset = i - window.find(data[i:i+seq_len])
                compressed_data += '(' + str(seq_len) + ',' + str(offset) + ')'
                window += data[i:i+seq_len]
                i += seq_len
            else:
                compressed_data += data[i]
                window += data[i]
                i += 1

            window = window[-self.window_size:]
        return compressed_data



if __name__ == "__main__":
    lz77 = LZ77(3, 100)
    data = 'abracadabra'
    print data
    print lz77.compress(data)

    data = 'Little Bunny Foo Foo \
Hopping through the forest \
Scooping up the field mice \
And boppin em on the head \
Down came the good fairy and she said \
Little Bunny Foo Foo \
I dont want to see you \
Scooping up the field mice \
And boppin em on the head \
Ill give you three chances \
And if you dont behave \
Ill turn you into a goon!'

    print data
    print lz77.compress(data)

