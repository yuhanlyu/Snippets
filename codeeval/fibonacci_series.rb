File.open(ARGV[0]).each_line do |line|
    n, even, odd = line.to_i, 0, 1;
    0.step(n - 1, 2) { |_| odd += even; even += odd }
    puts n % 2 == 0 ? even : odd
end
