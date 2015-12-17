bound = [-1, 2, 4, 11, 14, 18, 22, 65, 100, Float::INFINITY]
strs = ["This program is for humans", "Still in Mama's arms", 
        "Preschool Maniac", "Elementary school", "Middle school", 
        "High school", "College", "Working for the man", 
        "The Golden Years", "This program is for humans"]
File.open(ARGV[0]).each_line do |line|
    num = line.to_i
    puts strs[bound.index{|x| x >= num}]
end
