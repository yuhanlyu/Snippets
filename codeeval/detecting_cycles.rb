File.open(ARGV[0]).each_line do |line|
    nums = line.split.map(&:to_i)
    nums.each_with_object({}).each_with_index do |(x, h), i|
        if h.has_key?(x)
            puts nums[h[x]...i].join(" ")
            break
        else
            h[x] = i
        end
    end
end
