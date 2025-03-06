--A generalized RPN evaluator
--supported default operations: +, -, *, /, ^, negation, square root

import Data.List (foldl')
import qualified Data.Map as M

type Stack = [Double] --list of operands

--a single operation, takes a stack, returns a modified stack or an error message
type Operation = Stack -> Either String Stack 
type OpLookup = M.Map String Operation --operation lookup table

--function returns lookup table of default operations
defaultOps :: OpLookup
defaultOps = M.fromList [("+", binOp (+)), ("-", binOp (-)), ("*", binOp (*)),
   ("/", binOp (/)), ("^", binOp (**)), ("neg", unOp negate), ("sqrt", unOp sqrt)]

--unary operation handler
unOp :: (Double -> Double) -> Operation
unOp f (x:xs) = Right (f x:xs)
unOp _ _ = Left "Incorrect number of operands (expected: 1)"

--binary operation handler
binOp :: (Double -> Double -> Double) -> Operation
binOp f (x:y:ys) = Right (f y x:ys)
binOp _ _ = Left "Incorrect number of operands (expected: 2)"

--parse number, push on stack
parseNumber :: String -> Stack -> Either String Stack
parseNumber token stack =
   case reads token of
      [(a, "")] -> Right (a:stack)
      _ -> Left $ "Unknown token: " ++ token

--processes token as either operation or operand
processToken :: OpLookup -> Either String Stack -> String -> Either String Stack
processToken _ (Left err) _ = Left err
processToken ops (Right stack) token =
   case M.lookup token ops of
      Just op -> op stack --apply operation
      Nothing -> parseNumber token stack --parse number

--RPN evaluator
evaluateRPN :: OpLookup -> String -> Either String Double
evaluateRPN ops expression =
   case foldl' (processToken ops) (Right []) (words expression) of
      Right [result] -> Right result
      Right _ -> Left "Values left on stack (expected: 0)"
      Left err -> Left err
