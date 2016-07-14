#ifndef ROTATION_H
#define ROTATION_H

// Rotate an array circularly to the left by k positions
// This algorithm is from Jon Bentley's Programming Pearls.
void juggling_bentley(unsigned A[], unsigned n, unsigned k);

// Rotate an array circularly to the left by k positions
// This algorithm is from
// Ching-Kuang Shene,
// An Analysis of Two In-Place Array Rotation Algorithms
// The Computer Journal (1997) 40 (9): 541-546.
void juggling_shene(unsigned A[], unsigned n, unsigned k);

// Rotate an array circularly to the left by k positions
// This algorithm is from Jon Bentley's Programming Pearls.
void rotate_reverse(unsigned A[], unsigned n, unsigned k);

// Rotate an array circularly to the left by k positions
// This algorithm is from
// Ching-Kuang Shene,
// An Analysis of Two In-Place Array Rotation Algorithms
// The Computer Journal (1997) 40 (9): 541-546.
void block_swap_shene(unsigned A[], unsigned n, unsigned k);

// Rotate an array circularly to the left by k positions
// This algorithm is from
// David Gries and Harlan Mills,
// Swapping sections.
// Technical Report TR 81-452, Cornell University.
void block_swap_gries(unsigned A[], unsigned n, unsigned k);

#endif
