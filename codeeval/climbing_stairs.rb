File.open(ARGV[0]).each_line.map(&:to_i).each { |n|
    x, y, a, b = 1, 0, 1, 1
    while n > 0 do
        x, y = a * x + b * y, b * x + y * (a - b) if n % 2 == 1
        a, b, n = a * a + b * b, b * (2 * a - b), n >> 1
    end
    puts x
}
