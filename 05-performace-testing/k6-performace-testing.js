import http from 'k6/http';

export default function () {
  http.get('localhost/bar');
  http.get('localhost/foo');
}
