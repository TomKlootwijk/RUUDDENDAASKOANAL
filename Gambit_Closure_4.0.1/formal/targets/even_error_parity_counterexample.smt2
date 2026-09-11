; Tom Klootwijk Gambit 4.0 -- even_error_parity_counterexample
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const a Bool)(declare-const b Bool)
(assert (= (xor a b) (xor (not a) (not b))))
(check-sat)
(get-model)
