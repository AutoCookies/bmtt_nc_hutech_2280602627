class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # Create the empty rails
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # Start by moving down

        # Traverse through the plain_text
        for char in plain_text:
            rails[rail_index].append(char)

            # Change direction when we reach the top or bottom rail
            if rail_index == 0:
                direction = 1  # Move down
            elif rail_index == num_rails - 1:
                direction = -1  # Move up
            
            rail_index += direction

        # Join all the rails to create the cipher text
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Create the list of rail lengths
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        # Calculate the lengths of the rails
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Create the rails using the lengths
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # Reconstruct the plain text
        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index].pop(0)  # Pop the first character from the rail
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text
