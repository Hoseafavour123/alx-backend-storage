-- Creates an index on the table names and the firts
-- letter of names
CREATE INDEX idx_name_first ON names(name(1));
