File.open(ARGV[0]).each_line do |line|
    result = false
    digits = line.chomp.chars.map(&:to_i)
    if digits.length <= 10
        counts = digits.each_with_object(Array.new(10, 0)) {|d, o| o[d] += 1}
        result = (0..digits.length - 1).none? { |i| counts[i] != digits[i] }
    end
    puts result ? "1" : "0"
end
