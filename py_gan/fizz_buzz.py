import numpy as np
import tensorflow as tf

DIGITS = 20#二進制20bit


def binary_encode(num, digits=DIGITS):
    return [num >> i & 1 for i in range(digits)][::-1]#int to binary


def label_encode(num):
  if num % 15 == 0:
    return [1, 0, 0, 0]
  elif num % 3 == 0:
    return [0, 1, 0, 0]
  elif num % 5 == 0:
    return [0, 0, 1, 0]
  else:
    return [0, 0, 0, 1]


def get_data(num, low=101, high=10000):
  binary_num_list = []
  label_list = []
  for i in range(num):
    n = np.random.randint(low, high, 1)[0]#取101到10000之間一個int亂數
    binary_num_list.append(np.array(binary_encode(n)))#陣列擴增
    label_list.append(np.array(label_encode(n)))
  return np.array(binary_num_list), np.array(label_list)


def model(data):
  with tf.variable_scope('layer1') as scope:#隱藏層
    weight = tf.get_variable('weight', shape=(DIGITS, 512))# W維度 = [20,512]
    bias = tf.get_variable('bias', shape=(512,))#偏權值[512,0]
    x = tf.nn.relu(tf.matmul(data, weight) + bias)#活化函數relu( W * data + b)

  with tf.variable_scope('layer2') as scope:#隱藏層
    weight = tf.get_variable('weight', shape=(512, 100))# W維度 = [512,100]
    bias = tf.get_variable('bias', shape=(100,))#偏權值[100,0]
    x = tf.nn.relu(tf.matmul(x, weight) + bias)#活化函數relu( W * data + b)
    
  with tf.variable_scope('layer3') as scope:#輸出層
    weight = tf.get_variable('weight', shape=(100, 4))#W維度 = [100,4](4 labels)
    bias = tf.get_variable('bias', shape=(4,))#偏權值[4,0]
    x = tf.matmul(x, weight) + bias#輸出 = w * x + b

  return x


def main():
  data = tf.placeholder(tf.float32, shape=(None, DIGITS))#float32 data[0,20]
  label = tf.placeholder(tf.float32, shape=(None, 4))#float32 label[0,4]

  x = model(data)
  preds = tf.argmax(tf.nn.softmax(x), 1)#取softmax分類器得到機率值之最大值index
  acc = tf.reduce_mean(tf.cast(tf.equal(preds, tf.argmax(label, 1)), tf.float32))#比較預測值與實際值,轉float32加起來取平均
  loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=label, logits=x))#取得loss函數
  optimizer = tf.train.AdamOptimizer(0.01).minimize(loss)#Adam優化器降低loss更新weight,bias( learning rate: 0.01)

  with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())#初始化參數
    for step in range(3001):#訓練3000個step
      train_data, train_label = get_data(256)#一次256筆data
      _, a = sess.run([optimizer, acc], feed_dict={data: train_data, label: train_label})#算精確度
      if step % 300 == 0:
        print('Step: {} -> Accuracy: {:.3f}'.format(step, a))#每300個step印一次accuracy(小數點後三位)

    test_data = np.array([binary_encode(i) for i in range(1, 101)])#生成1到101的數列
    test_label = np.array([label_encode(i) for i in range(1, 101)])
    pred = sess.run(preds, feed_dict={data: test_data})#預測
    results = []
    for i in range(1, 101):
      results.append('{}'.format(['15倍', '3倍', '5倍', i][pred[i - 1]]))#印結果
    print(', '.join(results))#元素間隔
    _,b = sess.run([optimizer, acc], feed_dict={data: test_data, label: test_label})#算精確度
    print('Accuracy: {:.3f}'.format(b))#每300個step印一次accuracy(小數點後三位)


if __name__ == '__main__':#只運行該文件的main函式
    main()
