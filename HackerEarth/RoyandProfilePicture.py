"""
Roy and Profile Picture
Evaluate whether a photograph dimensions (W, H) given is within the dimensions provided L*L

Complexity:
Time and Space : O(1)
"""


def dim_checker(w, h, l):
    if w < l or h < l:
        print("UPLOAD ANOTHER")
    elif w == h:
        print("ACCEPTED")
    elif w > l or h > l:
        print("CROP IT")


num_of_photos = 3
given_dim = 180


for each_photo in range(num_of_photos):
    w, h = map(int, input().split())
    dim_checker(w, h, given_dim)





