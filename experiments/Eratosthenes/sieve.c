#include "sieve.h"

#include <math.h>
#include <string.h>

// The upper bound of the number of primes at most n.
// This formula is from the following paper:
// Pierre Dusart,
// The $k^{th}$ prime is greater than $k(\ln k +\ln\ln k -1)$ for $k\geq 2$,
// Mathematics of Computation, 8(225): 411-415 (1999)
static inline uint32_t upper_bound_of_pi(uint32_t n) {
    return (n / log(n)) * (1 + 1.2762 / log(n));
}

// Number of bytes having at least n + 1 bits.
static inline uint64_t bytes(uint64_t n) {
    return (n >> 4) + (((n >> 1) & 7) != 0);
}

// Mapping from the number to the index in the byte array.
static inline uint32_t number_to_index(uint32_t n) {
    return (n - 2) >> 1;
}

bool is_prime(uint32_t n, const bool prime[]) {
    return (n & 1) == 0 ? (n == 2) : (prime[number_to_index(n)] != 0);
}

static const uint32_t l1d_cache_size = 1 << 15;

void sieve(uint32_t n, bool prime[]) {
    memset(prime, 1, n >> 1);
    uint32_t bound = sqrt(n);
    for (uint32_t i = 3; i <= bound; i += 2) {
        if (prime[number_to_index(i)]) {
            for (uint32_t j = i * i; j <= n; j += (i << 1)) {
                prime[number_to_index(j)] = 0;
            }
        }
    }
}

void improved_sieve(uint32_t n, bool prime[]) {
    memset(prime, 1, n >> 1);
    uint32_t bound = sqrt(n);
    for (uint32_t i = 3; i <= bound; i += 2) {
        if (prime[number_to_index(i)]) {
            for (uint32_t k = n / i - (((n / i) & 1) == 0), j = i * k; 
                         k >= i; k -= 2, j -= (i << 1) ) {
                if (prime[number_to_index(k)]) {
                    prime[number_to_index(j)] = 0;
                }
            }
        }
    }
}

void linear_sieve(uint32_t n, bool prime[]) {
    memset(prime, 1, n >> 1);
    uint32_t bound = sqrt(n);
    sieve(bound, prime);
    uint32_t primes[upper_bound_of_pi(bound)], number_of_primes = 0;
    for (uint32_t i = 3; i <= bound; i += 2)
        if (prime[number_to_index(i)])
            primes[number_of_primes++] = i;
    for (uint32_t i = 3; i <= n / 3; i += 2) {
        for (uint32_t j = 0; j < number_of_primes && primes[j] <= n / i; ++j) {
            prime[number_to_index(primes[j] * i)] = 0;
            if (i % primes[j] == 0)
                break;
        }
    }
}

void segmented_sieve(uint32_t n, bool prime[]) {
    memset(prime, 1, n >> 1);
    uint32_t bound = sqrt(n);
    sieve(bound, prime);
    uint32_t primes[upper_bound_of_pi(bound)], number_of_primes = 0;
    for (uint32_t i = 3; i <= bound; i += 2)
        if (prime[number_to_index(i)])
            primes[number_of_primes++] = i;
    uint32_t next[number_of_primes], s = 0;
    uint32_t segment_size = l1d_cache_size;
    for (uint32_t low = bound + 1, 
                  high = low + segment_size > n ? n : low + segment_size;
         low <= n; low += segment_size) {
        for (uint32_t h = 0; h < number_of_primes; ++h) {
            uint32_t i = primes[h], j;
            if (i * i > high)
                break;
            if (h < s) {
                j = next[h];
            } else {
                j = ((low + (i - 1)) / i) * i;
                j += i * ((j & 1) == 0);
                ++s;
            }
            for (; j <= high; j += (i << 1)) {
                prime[number_to_index(j)] = 0;
            }
            next[h] = j;
        }
        high = (high + segment_size > n) ? n : high + segment_size;
    }
}

// Mapping from the number to the bit index
static inline uint64_t number_to_bit_index(uint64_t n) {
    return (n - 2) >> 1;
}

// Get the x-th bit in the bitset
static inline bool bit_get(uint64_t x, const uint32_t bitset[]) {
    return (bitset[x>>5] & (1 << (x&31))) != 0;
}

// Clear the x-th bit in the bitset
static inline void bit_reset(uint64_t x, uint32_t bitset[]) {
    bitset[x>>5] &= ~(1 << (x&31));
}

bool is_prime_bit(uint64_t n, const uint32_t bitset[]) {
    return (n & 1) == 0 ? (n == 2) :
               (bit_get(number_to_bit_index(n), bitset) != 0);
}

void sieve_bit(uint64_t n, uint32_t prime[]) {
    memset(prime, 0xFF, bytes(n));
    uint64_t bound = sqrtl(n);
    uint64_t max_index = number_to_bit_index(n);
    for (uint64_t i = 3, index = 0; i <= bound; i += 2, ++index) {
        if (bit_get(index, prime)) {
            for (uint64_t j_index = number_to_bit_index(i * i);
            j_index <= max_index; j_index += i) {
                bit_reset(j_index, prime);
            }
        }
    }
}

void improved_sieve_bit(uint64_t n, uint32_t prime[]) {
    memset(prime, 0xFF, bytes(n));
    uint64_t bound = sqrtl(n);
    for (uint64_t i = 3, index = 0; i <= bound; i += 2, ++index) {
        if (bit_get(index, prime)) {
            uint64_t k = n / i - ((n / i) % 2 == 0);
            uint64_t j_index = number_to_bit_index(i * k);
            for (int64_t k_index = number_to_bit_index(k);
                 k_index >= (int64_t)index; j_index -= i, --k_index) {
                if (bit_get(k_index, prime))
                    bit_reset(j_index, prime);
            }
        }
    }
}

void linear_sieve_bit(uint64_t n, uint32_t prime[]) {
    memset(prime, 0xFF, bytes(n));
    uint64_t bound = sqrtl(n);
    sieve_bit(bound, prime);
    uint32_t primes[upper_bound_of_pi(bound)], number_of_primes = 0;
    for (uint32_t i = 3, index = 0; i <= bound; i += 2, ++index)
        if (bit_get(index, prime))
            primes[number_of_primes++] = i;
    for (uint64_t i = 3; i <= n / 3; i += 2) {
        for (uint32_t j = 0; j < number_of_primes && primes[j] <= n / i; ++j) {
            bit_reset(number_to_bit_index(primes[j] * i), prime);
            if (i % primes[j] == 0)
                break;
        }
    }
}

void segmented_sieve_bit(uint64_t n, uint32_t prime[]) {
    memset(prime, 0xFF, bytes(n));
    uint64_t bound = sqrtl(n);
    sieve_bit(bound, prime);
    uint32_t primes[upper_bound_of_pi(bound)], number_of_primes = 0;
    for (uint32_t i = 3, index = 0; i <= bound; i += 2, ++index)
        if (bit_get(index, prime))
            primes[number_of_primes++] = i;
    uint64_t next[number_of_primes], s = 0;
    uint64_t segment_size = l1d_cache_size << 7;
    for (uint64_t low = bound + 1, 
                  high = low + segment_size > n ? n : low + segment_size;
         low <= n; low += segment_size) {
        uint64_t high_index = number_to_bit_index(high);
        for (uint64_t h = 0; h < number_of_primes; ++h) {
            uint64_t i = primes[h], j_index;
            if (i * i > high)
                break;
            if (h < s) {
                j_index = next[h];
            } else {
                uint64_t j = ((low + (i - 1)) / i) * i;
                j += i * ((j & 1) == 0);
                j_index = number_to_bit_index(j);
                ++s;
            }
            for (; j_index <= high_index; j_index += i) {
                bit_reset(j_index, prime);
            }
            next[h] = j_index;
        }
        high = (high + segment_size > n) ? n : high + segment_size;
    }
}

// These variables are used for wheel factorization.
// Wheel factorization removes all integers that are not relatively prime
// to the given wheel_primes.
// For example, if the wheel_primes[] = {2}, then all even numbers will be
// ignores.
// For each integer x that are relatively prime to the given wheel_primes,
// wheel_index(x) will be the index of the integer in the bitset.
// For example, if wheel_primes[] = {2}, then wheel_index(x) = (x - 2) / 2.
// In order to compute the wheel_index, let the primorial be the product of 
// all wheel_primes, number_of_coprimes be the number of integers that are 
// relatively prime to all wheel_primes, and coprime_indices be the array of 
// length primorial, where coprime_indices[i] is the number of integers < x 
// that are relatively prime to wheel_primes.
// For example, if wheel_primes[] = {2, 3}, then
//    coprime_indices[] = {0, 0, 1, 1, 1, 1}.
// For an integer x = q * primorial + m that is relatively prime to
// wheel_primes, where m = q % primorial, x's wheel_inex will be 
//     q * number_of_coprimes + coprime_indices[m].
// Thus, we usually consider x as a pair(q, coprime_indices[m]), where
//    m = q % primorial, and 
// coprime_indices[m] is usually called step_index of x in the program.
//
// During the process of sieve, we need to find the integer y corresponding
// to the index of wheel_index(x) + 1.
// That is, the integer y corresponding to the index of wheel_index(x) + 1 is
// either 
// (q, coprime_indices[m] + 1) if coprime_indices[m] + 1 < number_of_coprimes
// or (q + 1, 0).
// Thus, the y - x is just the diference of the coprimes indexed by the 
// coprime_indices.
// Hence, we can store the difference from the coprimes to the next coprimes in
// a steps array.
// For example, if wheel_primes[] = {2, 3}, then steps[] = {4, 2}, since
// only 6n + 1 and 6n - 1 are considered.
// Using steps array, y = x + steps[next_step_index(coprime_indices[m])].
//
// During the process of sieve, we also need the following operation:
//    Given the index of integer j * k,
//        where both j and k are relatively prime to wheel_primes
//    find the index of j * h, where h has index = wheel_index(k) + 1.
// Let x = j * k, j is represented by (q_j, coprime_indices[m_j]), 
// and k is represented by (q_k, coprime_indices[m_k]),
// then the index of j * h will be
//    (q_j / primorial) * base_increment[coprime_indices[m_k]] +
//        increments[coprime_indices[m_j]][coprime_indices[m_k]]
// The tables of base_increment and increments can be generated by precompute.
// The idea of computing base_increment and increments is as follows:
// Let j = primorial * q_j + m_j, k = primorial * q_k + m_k.
// Since h - k = steps[m_k], 
//     j * (h - k) = primorial * q_j * steps[m_k] + m_j * steps[m_k].
// Thus, we use base_increment[i] = wheel_index(primorial * steps[i]).
// Let coprimes be the array of all integers that are smaller than primorial
//    and relatively prime to wheel_primes.
// We use increments[coprime_indices[a]][coprime_indices[b]] = 
//     the increment of index from a * b to a * (b + steps[b]), for all
//     a and b in coprimes.

// The following variables can be computed by using precompute method.
// However, programs will be more efficient if primorial and number_of_coprimes 
// are fixed as constants.
// 
// Primes used for wheel.
// static const uint64_t wheel_primes[] = {2, 3, 5, 7};
//
// The product of all primes used for wheel.
// static const uint64_t primorial = 210;
//
// The number of integers from 1 to primorial that are relative prime to 
// all wheel_primes.
// static const uint64_t number_of_coprimes = 48;
//
// The next number corresponding to the next wheel_index.
// static uint64_t steps[48];
//
// Mapping from all integers from 0 to primorial to the index of the next
// coprimes.
// static uint64_t coprime_indices[210];
//
// The difference from the integer to the next coprimes.
// static uint64_t need[210];
//
// The amount of increments of index from j * k to j * (k + 1).
// static uint64_t base_increment[48];
// static uint64_t increments[48][48];

// The following is for 210-wheel.
// static const uint64_t wheel_primes[] = {2, 3, 5, 7};
// static const uint64_t primorial = 210;
// static const uint64_t number_of_coprimes = 48;
// static uint64_t steps[48];
// static uint64_t coprime_indices[210];
// static uint64_t need[210];
// static uint64_t base_increment[48];
// static uint64_t increments[48][48];

// The following is for 6-wheel.
/*
static const uint64_t wheel_primes[] = {2, 3};
static const uint64_t primorial = 6;
static const uint64_t number_of_coprimes = 2;
static const uint64_t steps[2] = {4, 2};
static const uint64_t coprime_indices[6] = {0, 0, 1, 1, 1, 1};
static const uint64_t need[6] = {1, 0, 3, 2, 1, 0};
static const uint64_t base_increment[2] = {8, 4};
static const uint64_t increments[2][2] = {{1, 1}, {7, 3}};
*/

// The following is for 30-wheel
static const uint64_t primorial = 30;
static const uint64_t coprime_indices[] = {
    0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 
    2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 
    6, 6, 6, 6, 7, 7, 7, 7, 7, 7};

static const uint64_t steps[] =  {6, 4, 2, 4, 2, 4, 6, 2};
static const uint64_t number_of_coprimes = 8;
static const uint64_t base_increment[] = {
    48, 32, 16, 32, 16, 32, 48, 16};
static const uint64_t increments[][8] = {
    {1, 1, 1, 1, 1, 1, 1, 1 },
    {12, 7, 4, 7, 4, 7, 12, 3}, 
    {18, 12, 6, 11, 6, 12, 18, 5}, 
    {21, 14, 7, 13, 7, 14, 21, 7}, 
    {27, 18, 9, 19, 9, 18, 27, 9}, 
    {30, 20, 10, 21, 10, 20, 30, 11}, 
    {36, 25, 12, 25, 12, 25, 36, 13}, 
    {47, 31, 15, 31, 15, 31, 47, 15}};
static const uint64_t need[] = {
    1, 0, 5, 4, 3, 2, 1, 0, 3, 2, 
    1, 0, 1, 0, 3, 2, 1, 0, 1, 0, 
    3, 2, 1, 0, 5, 4, 3, 2, 1, 0};

// Mapping from the number to the index.
static inline uint64_t wheel_index(uint64_t n) {
    // This is for 30-wheel only.
    return (n << 2) / 15;
    // This is for 6-wheel only.
    // return (n << 1) / 6;
    // General case.
    // return (n / primorial) * number_of_coprimes + 
    //      coprime_indices[n % primorial];
} 

// Find the next index step
static inline uint32_t next_step_index(uint32_t index) {
    return ++index % number_of_coprimes;
}

bool is_prime_wheel(uint32_t n, const bool prime[]) {
    // This is for 30-wheel only
    if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0)
        return n == 2 || n == 3 || n == 5 || n == 7;
    return prime[wheel_index(n)];

    // General case.
    // for (uint64_t i = 0; i < sizeof(wheel_primes) / sizeof(wheel_primes[0]);
    //   ++i) {
    //   if (n % wheel_primes[i] == 0)
    //        return n == wheel_primes[i];
    // }
    // return prime[wheel_index(n)];
}

bool is_prime_wheel_bit(uint64_t n, const uint32_t bitset[]) {
    // This is for 30-wheel only
    if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0)
        return n == 2 || n == 3 || n == 5 || n == 7;
    return bit_get(wheel_index(n), bitset);

    // General case.
    // for (uint64_t i = 0; i < sizeof(wheel_primes) / sizeof(wheel_primes[0]);
    //    ++i) {
    //    if (n % wheel_primes[i] == 0)
    //         return n == wheel_primes[i];
    // }
    // return bit_get(wheel_index(n), bitset);
}

void wheel_sieve(uint32_t n, bool prime[]) {
    uint32_t bound = sqrt(n);
    uint32_t max_index = wheel_index(n);
    memset(prime, 1, n >> 1);

    uint32_t step_index = 1;
    for (uint32_t i = steps[0] + 1, index = 1; i <= bound; ++index) {
        if (prime[index]) {
            uint32_t quo = i / primorial, mod = i % primorial;
            uint32_t inc[number_of_coprimes], m_step_index = step_index;
            for (uint32_t j = 0; j < number_of_coprimes; ++j) {
                inc[j] = increments[coprime_indices[mod]][j] + 
                         quo * base_increment[j];
            }
            for (uint32_t j_index = wheel_index(i * i); j_index <= max_index;) {
                prime[j_index] = false;
                j_index += inc[m_step_index];
                m_step_index = next_step_index(m_step_index);
            }
        }
        i += steps[step_index];
        step_index = next_step_index(step_index);
    }
}

void segmented_wheel_sieve(uint32_t n, bool prime[]) {
    uint32_t bound = sqrt(n);
    uint32_t max_index = wheel_index(n);
    memset(prime, 1, n >> 1);

    wheel_sieve(bound, prime);
    uint32_t primes[upper_bound_of_pi(bound)], number_of_primes = 0;
    uint32_t step_index = 1, bound_index = wheel_index(bound);
    for (uint32_t i = steps[0] + 1, index = 1; 
         index <= bound_index; ++index)  {
        if (prime[index]) {
            primes[number_of_primes++] = i;
        }
        i += steps[step_index];
        step_index = next_step_index(step_index);
    }    
    uint32_t next[number_of_primes];
    uint32_t next_step[number_of_primes];
    uint32_t segment_size = l1d_cache_size >> 1;
    for (uint32_t low = bound + 1, s = 0,
                  high = low + segment_size > n ? n : low + segment_size;
         low <= n; low += segment_size) {
        uint32_t high_index = wheel_index(high);
        for (uint32_t h = 0; h < number_of_primes; ++h) {
            uint32_t i = primes[h], j_index;
            if (i * i > high)
                break;
            if (h < s) {
                j_index = next[h];
                step_index = next_step[h];
            } else {
                uint64_t m = ((low + (i - 1)) / i);
                m += need[m % primorial];
                step_index = coprime_indices[m % primorial];
                j_index = wheel_index(m * i);
                ++s;
            }
            if (j_index <= high_index) {
                uint64_t quo = i / primorial, mod = i % primorial;
                while (j_index <= high_index) {
                    prime[j_index] = false;
                    j_index += increments[coprime_indices[mod]][step_index] +
                               quo * base_increment[step_index];
                    step_index = next_step_index(step_index);
                }
            }
            next[h] = j_index;
            next_step[h] = step_index;
        }
        high = (high + segment_size > n) ? n : high + segment_size;
    }
}

void wheel_bit(uint64_t n, uint32_t prime[]) {
    uint64_t bound = sqrtl(n);
    uint64_t max_index = wheel_index(n);
    memset(prime, 0xFF, (max_index >> 3) + 1);

    uint32_t step_index = 1;
    for (uint64_t i = steps[0] + 1, index = 1; i <= bound; ++index) {
        if (bit_get(index, prime)) {
            uint64_t quo = i / primorial, mod = i % primorial;
            uint32_t inc[number_of_coprimes], m_step_index = step_index;
            for (uint32_t j = 0; j < number_of_coprimes; ++j) {
                inc[j] = increments[coprime_indices[mod]][j] + 
                         quo * base_increment[j];
            }
            for (uint64_t j_index = wheel_index(i * i); j_index <= max_index;) {
                bit_reset(j_index, prime);
                j_index += inc[m_step_index];
                m_step_index = next_step_index(m_step_index);
            }
        }
        i += steps[step_index];
        step_index = next_step_index(step_index);
    }
}

void segmented_wheel_bit(uint64_t n, uint32_t prime[]) {
    uint64_t bound = sqrtl(n);
    uint64_t max_index = wheel_index(n);
    memset(prime, 0xFF, (max_index >> 3) + 1);

    wheel_bit(bound, prime);
    uint32_t primes[upper_bound_of_pi(bound)], number_of_primes = 0;
    uint32_t step_index = 1, bound_index = wheel_index(bound);
    for (uint32_t i = steps[0] + 1, index = 1; 
         index <= bound_index; ++index)  {
        if (bit_get(index, prime)) {
            primes[number_of_primes++] = i;
        }
        i += steps[step_index];
        step_index = next_step_index(step_index);
    }    
    uint64_t next[number_of_primes];
    uint32_t next_step[number_of_primes];
    uint64_t segment_size = l1d_cache_size << 6;
    for (uint64_t low = bound + 1, s = 0,
                  high = low + segment_size > n ? n : low + segment_size;
         low <= n; low += segment_size) {
        uint64_t high_index = wheel_index(high);
        for (uint32_t h = 0; h < number_of_primes; ++h) {
            uint64_t i = primes[h], j_index;
            if (i * i > high)
                break;
            if (h < s) {
                j_index = next[h];
                step_index = next_step[h];
            } else {
                uint64_t m = ((low + (i - 1)) / i);
                m += need[m % primorial];
                step_index = coprime_indices[m % primorial];
                j_index = wheel_index(m * i);
                ++s;
            }
            if (j_index <= high_index) {
                uint64_t quo = i / primorial, mod = i % primorial;
                while (j_index <= high_index) {
                    bit_reset(j_index, prime);
                    j_index += increments[coprime_indices[mod]][step_index] +
                               quo * base_increment[step_index];
                    step_index = next_step_index(step_index);
                }
            }
            next[h] = j_index;
            next_step[h] = step_index;
        }
        high = (high + segment_size > n) ? n : high + segment_size;
    }
}

/*
void precompute(const uint64_t primes[], uint64_t n) {
    primorial = 1;
    for (uint32_t i = 0; i < n; ++i) {
        primorial *= primes[i];
    }
    bool is_coprime[primorial + 1];
    is_coprime[0] = is_coprime[1] = false;
    number_of_coprimes = 0;
    for (uint32_t i = 1; i < primorial; ++i) {
        bool divisible = false;
        for (uint32_t j = 0; j < n; ++j)
            if (i % primes[j] == 0)
                divisible = true;
        is_coprime[i] = !divisible;
        if (is_coprime[i])
            ++number_of_coprimes;
    }
    uint32_t coprimes[number_of_coprimes], s = 0;
    coprime_indices[0] = 0;
    for (uint32_t i = 1; i < primorial; ++i) {
        coprime_indices[i] = s;
        if(is_coprime[i]) {
            coprimes[s++] = i;
        }
    }
    for (uint32_t i = 0; i < s - 1; ++i)
        steps[i] = coprimes[i + 1] - coprimes[i];
    steps[s - 1] = primorial - coprimes[s - 1] + coprimes[0];
    for (uint64_t i = 0; i < number_of_coprimes; ++i) {
        uint64_t base = wheel_index(coprimes[i]), acc = 1;
        for (uint64_t j = 0; j < number_of_coprimes; ++j) {
            uint64_t temp = wheel_index(coprimes[i] * (acc + steps[j]));
            increments[i][j] = temp - base;
            base = temp;
            acc += steps[j];
        }
        base_increment[i] = wheel_index(steps[i] * primorial);
    }
    uint32_t next = 0;
    for (uint32_t i = 0; i < primorial; ++i) {
        need[i] = coprimes[next] - i;
        if (need[i] == 0)
            ++next;
    }
    std::cout << "primorial: " << primorial << '\n';
    std::cout << "number_of_coprimes: " << number_of_coprimes << '\n';
    for (uint32_t i = 0; i < number_of_coprimes; ++i)
        std::cout << coprimes[i] << ", ";
    std::cout << "\ncoprime_indices:";
    for (uint32_t i = 0; i < primorial; ++i)
        std::cout << coprime_indices[i] << ", ";
    std::cout << "\nsteps:";
    for (uint32_t i = 0; i < number_of_coprimes; ++i)
        std::cout << steps[i] << ", ";
    std::cout << "\nbase_increment:";
    for (uint32_t i = 0; i < number_of_coprimes; ++i)
        std::cout << base_increment[i] << ", ";
    std::cout << "\nincrement:";
    for (uint32_t i = 0; i < number_of_coprimes; ++i) {
        for (uint32_t j = 0; j < number_of_coprimes; ++j)
            std::cout << increments[i][j] << ", ";
        std::cout << '\n';
    }
    std::cout << "need: ";
    for (uint32_t i = 0; i < primorial; ++i)
        std::cout << need[i] << ", ";
    std::cout << '\n';
    for (uint32_t i = 0; i < number_of_coprimes; ++i)
        std::cout << wheel_index(coprimes[i]) << ' ';
    std::cout << '\n';
}
*/
